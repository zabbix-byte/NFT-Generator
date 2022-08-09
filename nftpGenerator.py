from app.image_loader import ImageLoader

# libs
import json
import os
import sys


def main(generate=1):
    print("""
          ______     _     _     _      
         |___  /    | |   | |   (_)     
            / / __ _| |__ | |__  ___  __
           / / / _` | '_ \| '_ \| \ \/ /
          / /_| (_| | |_) | |_) | |>  < 
         /_____\__,_|_.__/|_.__/|_/_/\_\\
                                                           
               _   _ ______ _______ 
              | \ | |  ____|__   __|
              |  \| | |__     | |   
              | . ` |  __|    | |   
              | |\  | |       | |   
              |_| \_|_|       |_|   
                                    
                                  _             
                                 | |            
   __ _  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
  / _` |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
 | (_| |  __/ | | |  __/ | | (_| | || (_) | |   
  \__, |\___|_| |_|\___|_|  \__,_|\__\___/|_|   
   __/ |                                        
  |___/    
    """)
    file_config = open(os.path.dirname(
        os.path.abspath(__file__))+'/config_app.json', 'r')
    file_config = json.load(file_config)
    for i in range(generate):
        img_n = ImageLoader(n=i,
                            base_image=file_config['Base template'],
                            components_types=file_config['Types components'],
                            complements=file_config['Components'], backgrounds=file_config['Backgrounds'])

        img_n.put_components_in_position()
        img_n.save()


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('You need to pass the amount of NFT you want to generate')
        exit()
    try:
        int(sys.argv[1])
    except:
        print('The value of first parameter need to be a number')
        exit()
    main(int(sys.argv[1]))
