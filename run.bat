conda env create -f environment.yml
CALL conda.bat activate base
pip install -r requirements.txt -i https://pypi.douban.com/simple
cd ./testCase
pytest
pause