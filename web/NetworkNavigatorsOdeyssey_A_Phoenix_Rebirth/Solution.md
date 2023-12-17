# NetworkNavigatorsOdeyssey_A_Phoenix_Rebirth
## Write up

we were given this flask app
```py
from flask import Flask, render_template, request
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def ip():
    option = request.form['option']
    # Check that user input doesn't contain any spaces
    if " " in option:
        return "No spaces are allowed."
    # Double the check by spliting user input into an array before passing it securely to subprocess.check_output()
    option = ['/sbin/ip'] + option.split()
    
    try:
        # Use shell=False to prevent any shell injections
        result = subprocess.check_output(option, text=True,timeout=1,stderr=subprocess.STDOUT, shell=False)
        return f'{result}'
    except subprocess.CalledProcessError as e:
        return f'Error: {e.output}'
    except Exception as e:
        return f"Error {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)

```

the program takes our input split it and excute the ip command with our arguemt

how we can trick it to read the flag we cant inject commands because **shell=False**
but we can inject argument there is a cool website that can help finds something interesting
https://gtfobins.github.io/

we find that we can use this argument to read a file
```
-force -batch FILE
```

so will pass this 
```
-force -batch /flag.txt
```

but there is a check for spaces on our unput so can we bypass that 

of corse we can do that by replacing the space with a tab

here is the final soltion

```
-force	-batch	/flag.txt
```

here is the flag : shellmates{5laugh73r_7h3_Pho3niXx!___1njec7_1T_w1tH_@rgum3ntSs!!}



