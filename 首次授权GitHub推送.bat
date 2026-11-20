@echo off
chcp 65001 >nul
title GitHub 登录授权与初次推送

echo ========================================================
echo       FootHub · 懂球云 - 首次 GitHub 授权推送
echo ========================================================
echo.
echo 即将为您推送到 https://github.com/Galen7749/fm26-virton-hub.git
echo 如果弹出浏览器授权窗口，请点击 [Sign in with your browser] 一键授权。
echo.

cd /d "I:\fm26-virton-hub"
git push -u origin main

echo.
if %errorlevel% equ 0 (
    echo [✓] 恭喜！代码已成功推送到 GitHub！
) else (
    echo [!] 推送遇到问题，请检查是否已在浏览器中完成 GitHub 授权。
)
echo.
pause
