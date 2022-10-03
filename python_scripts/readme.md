## Setting Up Your Python Environment
If you don't already have Python installed on your system, then download it from [here](https://www.python.org/downloads/). Then follow these steps to clone the Git repository for this course and set up a Python Virtual Environment to run the scripts in (they assume you also have [Git](https://github.com/git-guides/install-git) installed):

1. Clone the NetBox Zero to Hero Git repository and change into the `python_scripts` directory:
```
git clone https://github.com/richbibby-NS1/netbox-zero-to-hero.git
cd netbox-zero-to-hero/python_scripts
```

2. Create a new Python Virtual Environment and activate it: 
```
python3 -m venv .
source bin/activate
```
3. Install `python-dotenv` which will be used to load environment variables from a `.env` file. This allows you to use credentials and API tokens in your scripts, without having them appear in the actual code:
```
pip3 install python-dotenv
```
4. Rename file `.env.example` to `.env` **Important** - remember to add .env to your .gitignore file to avoid uploading the file with your api token in it to your Git repository if you are pushing code back to your own public Git repository. 
```
mv .env.example .env
```
5. Edit the file `.env` and ddd your API token
``` 
api_token = "<YOUR NETBOX API TOKEN>"
```
6. When you have finished working with the scripts, deactivate the Python virtual environment:
```
deactivate
```