https://play.picoctf.org/practice/challenge/431?category=3&page=1

Description
This challenge is a little bit invasive. It will try to fight your debugger. 
With that in mind, debug the binary and get the flag! This challenge executable is a GUI application and it requires admin privileges. 
And remember, the flag might get corrupted if you mess up the process's state. Challenge can be downloaded here. Unzip the archive with the password picoctf If you get "VCRUNTIME140D.dll" and "ucrtbased.dll" missing error, 
then that means the Universal C Runtime library and Visual C++ Debug library are not installed on your Windows machine. The quickest way to fix this is:

    Download Visual Studio Community installer from https://visualstudio.microsoft.com/vs/community/
    After the installer starts, first select 'Desktop development with C++' and then, in the right side column, select 'MSVC v143 - VS 2022 C++ x64/x86 build tools' and 'Windows 11 SDK' packages.

This will take ~30 mins to install any missing DLLs. 