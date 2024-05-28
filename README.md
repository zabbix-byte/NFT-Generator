**This is an open source project that allows you to generate NFT from a base template and plugins.**


# 🦧 **Usage** 
All the imagenes need to be PNG
1. You need to generate a base design
2. You need to generate backgrounds (Important that they are of the same resolution as the base design)
3. You have to declare the types of components that the NFT will have (hat, glasses ... what you want)
4. You have to say where the component is located and its type

**Where is this configured?**
```
config_app.json
```
Edit the file with the requirements above and with the same keys that you will find

Example:
```json
{
    "Base template": "images/capy.png",
    "Backgrounds": ["images/fundal.png"],
    "Types components": ["skirt", "glasses", "hat"],
    "Components": [
        {"file":"images/funda.png", "type": "skirt"},
        {"file":"images/sapca.png", "type": "hat"}
    ]
}
```

How to run the app:

The app are in a very early phase, it does not have a compiled version, you will have to install the `requirements.txt` and run the application in python

```sh
pip install -r requirements.txt # This is use to install the requirements of the app
python nftpGenerator.py 10 # the "10" is the number of nft will be generated
