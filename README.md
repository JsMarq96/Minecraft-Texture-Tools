# Minecraft-Texture-Downscaler
This is the first of a series of tool I am developing in order to optimize the workflow of the artist @del_cieno foor the Minecraft texturepack NAPP.<br/>
Since as of now, the texture pack comes in 2 version, with 2 resolutions, I created this tool for a quick and easy downscale, avoding him the pain of downscaling all the texture and maps one by one.
## How to run it
If you want to execute it in the console just: <br/>
`python3 TexPackResize.py`<br/>
And a menu will be prompted.<br/>
If you want to use the GUI, then just type in the console:<br/>
`python3 GUI.py`<br/>
## How does it work
First, it duplicates the whole folder structure that was selected; then it searches for all the files with formats .jpg and .png; and starts reescaling and replacing them in the new copy of the folder, while using bicubic interpolation.
## Dependencies
- Python 3
- TkInter
- PIL
- SHutil
- PyPng
