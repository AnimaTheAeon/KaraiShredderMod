@echo off
title Karai + Shredder Mod
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0KaraiShredderMod.ps1"
if errorlevel 1 pause
