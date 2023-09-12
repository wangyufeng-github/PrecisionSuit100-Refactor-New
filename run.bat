@REM 停止当前运行的conda环境
@REM CALL conda.bat deactivate
@REM conda env remove --name base
@REM conda env create -f environment.yml
@REM CALL conda.bat activate base
pip install -r requirements.txt -i https://pypi.douban.com/simple
cd ./testCase
pytest
pause