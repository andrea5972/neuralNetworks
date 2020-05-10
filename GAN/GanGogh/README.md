
# Modern Art with GanGogh

**Author:** Andrea Murphy
  
**Description**: Modern art created using generative adversarial network (GAN) as an art medium. Inspired by and built off the work and research of Kenny Jones and Derrick Bonafilia. Their code associated with the GanGogh project can be found on the GitHub repository below.

[“GANGogh: Creating Art with GANs”.](https://github.com/rkjones4/GANGogh)

## Implementation


 1. **Gather the Training Data:**
 

	[GanGogh’s](http://academictorrents.com/details/1d154cde2fab9ec8039becd03d9bb877614d351b) training dataset


 2. **Prepare the Training Data:**

Use `preProcess.py` to create image datasets of 64 by 64 pixels images from the downloaded wikiart data.


 3. **Modify the Files**
 


The styles variable in /wikiartGenre.py as follows:
    
    styles = {
    
    'abstract': 14999,
    
    'animal-painting': 1798,
    
    'cityscape': 6598,
    
    'figurative': 4500,
    
    'flower-painting': 1800,
    
    'genre-painting': 14997,
    
    'landscape': 15000,
    
    'marina': 1800,
    
    'mythological-painting': 2099,
    
    'nude-painting-nu': 3000,
    
    'portrait': 14999,
    
    'religious-painting': 8400,
    
    'still-life': 2996,
    
    'symbolic-painting': 2999
    
    }
    
 
 
    
