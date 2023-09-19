pip install -r requirements.txt -q
cd testCase
pytest -sv --alluredir=../outFiles/reports/tmp --clean-alluredir
pause