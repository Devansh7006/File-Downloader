try:
    import requests
except ModuleNotFoundError:
        import sys , subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])

url = input("Enter The URL :").strip()
name = input("Enter Name of the file with extension(.png/.jpg etc.) :").strip()
try:
    r = requests.get(url, allow_redirects=True)
    with open(name, 'wb') as f:
        f.write(r.content)
    print(f"\n✅ File saved as: {name}")
except Exception as e:
    print(f"\n❌ Failed to download file: {e}")
