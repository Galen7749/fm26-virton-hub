@echo off
chcp 65001 >nul
title FootHub · 懂球云 | FM 战报一键自动同步

echo ========================================================
echo        FootHub · 懂球云 - FM 数据自动同步流水线
echo ========================================================
echo.

cd /d "I:\fm26-virton-hub"

if not exist "venv\Scripts\python.exe" (
    echo [错误] 未找到 Python 虚拟环境，请检查 I:\fm26-virton-hub\venv
    pause
    exit /b 1
)

"venv\Scripts\python.exe" "scripts\sync_fm.py"

echo.
echo 按任意键退出本窗口...
pause >nul
