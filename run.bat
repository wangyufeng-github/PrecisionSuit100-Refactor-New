python -m venv venv
Set-ExecutionPolicy RemoteSigned
venv\Scripts\Activate
pip install -r requirements.txt -i https://pypi.douban.com/simple
cd ./testCase
pytest
deactivate
