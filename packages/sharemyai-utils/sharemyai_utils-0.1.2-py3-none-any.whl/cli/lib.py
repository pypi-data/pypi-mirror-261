import asyncio
from dotenv import load_dotenv, set_key
import os
import json
import requests
import subprocess
import sys

from cli.fingerprint import get_fingerprint
base_url = "https://sharemyai-next-production.up.railway.app/api"
dotenv_path = '.env'
load_dotenv(dotenv_path)

# saves a session token for future calls and writes it to .env as SESSION_TOKEN
def login_with_token(token):
    # Check if SESSION_TOKEN already exists and update it; otherwise, add it
    if 'SESSION_TOKEN' in os.environ:
        set_key(dotenv_path, 'SESSION_TOKEN', token)
    else:
        with open(dotenv_path, 'a') as file:
            file.write(f'SESSION_TOKEN={token}\n')
    user = get_current_user()
    if not user:
         # remove the token from .env
        set_key(dotenv_path, 'SESSION_TOKEN', '')
        print("Login failed. Please try again.")
        return False
    return user

def get_current_user():
    token = os.getenv('SESSION_TOKEN')
    if not token:
        print("No session token found. Please login first.")
        return
    response = requests.get(f"{base_url}/user", headers={"Authorization": f"Bearer {token}"})
    return response.json()

def post_register_worker(pluginId):
    token = os.getenv('SESSION_TOKEN')
    if not token:
        print("No session token found. Please login first.")
        return
    fingerprint_bytes = asyncio.run(get_fingerprint())
    fingerprint_str = fingerprint_bytes.hex()
    response = requests.post(f"{base_url}/plugin/worker", headers={"Authorization": f"Bearer {token}"}, json={"fingerprint": fingerprint_str, "pluginId": pluginId})
    return response.json()
 
def get_my_workers():
    token = os.getenv('SESSION_TOKEN')
    if not token:
        print("No session token found. Please login first.")
        return
    response = requests.get(f"{base_url}/plugin/worker", headers={"Authorization": f"Bearer {token}"})
    return response.json()



def get_and_download_plugin(pluginId):
    token = os.getenv('SESSION_TOKEN')
    if not token:
        print("No session token found. Please login first.")
        return
    response = requests.get(f"{base_url}/plugin?id={pluginId}", headers={"Authorization": f"Bearer {token}"})
    remotePlugin = response.json()
    if not remotePlugin:
        raise Exception(f"Could not find plugin with id {pluginId}")
    
    pluginPath = remotePlugin['name']
    if not os.path.exists(pluginPath):
        os.makedirs(pluginPath, exist_ok=True)
    
    modelJson = {
        "name": remotePlugin['name'],
        "description": remotePlugin['description'],
        "isPublic": remotePlugin['isPublic'],
        "remoteUrl": remotePlugin['remoteUrl'],
        "capabilities": remotePlugin['capabilities'],
        "requirements": remotePlugin['requirements'],
        "torchRequirements": remotePlugin['torchRequirements'],
        "params": remotePlugin['params'],
    }
    
    runPyPath = os.path.join(pluginPath, 'run.py')
    modelJsonPath = os.path.join(pluginPath, 'model.json')
    with open(runPyPath, 'w') as run_py:
        run_py.write(remotePlugin['code'])
    with open(modelJsonPath, 'w') as model_json:
        json.dump(modelJson, model_json, indent=2)
    
    return remotePlugin, pluginPath

def create_venv(plugin_path):
    venv_path = os.path.join(plugin_path, 'venv')
    if not os.path.exists(venv_path):
        subprocess.check_call([sys.executable, "-m", "venv", venv_path])
    return venv_path

def install_requirements(venv_path, requirements_list):
    pip_path = 'Scripts' if os.name == 'nt' else 'bin'
    subprocess.check_call([os.path.join(venv_path, pip_path, 'pip'), 'install', "sharemyai-utils", *requirements_list])

def install_torch_requirements(venv_path, dependencies):
    pip_path = 'Scripts' if os.name == 'nt' else 'bin'
    torch_index_url = "https://download.pytorch.org/whl/cu118"
    print("Installing torch dependencies from", torch_index_url)
    subprocess.check_call([os.path.join(venv_path, pip_path, 'pip'), 'install'] + dependencies + ["--index-url", torch_index_url])
    
def run_plugin(venv_path, plugin_path):
    pip_path = 'Scripts' if os.name == 'nt' else 'bin'
    process = subprocess.Popen([os.path.join(venv_path, pip_path, 'python'), os.path.join(plugin_path, 'run.py')])
    try:
        process.wait()
    except KeyboardInterrupt:
        process.terminate()
        process.wait()

