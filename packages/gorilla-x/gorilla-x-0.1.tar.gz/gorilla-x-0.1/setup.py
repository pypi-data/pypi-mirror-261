from setuptools import setup, find_packages
import sys
from os import path

sys.path.append(path.dirname(path.realpath(__file__)))


# from distutils.core import setup
setup(
  name = 'gorilla-x',        
  packages = ['demo', 'docker', 'exec_engine', 'authorizations'],
  version = '0.1',      
  description = 'CLI for Gorilla Execution Engine',  
  author = "Shishir Patil, Noppapon Chalermchockcharoenkit, Roy Huang, Liheng Lai, Aaron Hao",   
  url = "https://github.com/gorilla-llm/exec-engine",   
  download_url = "https://github.com/gorilla-llm/exec-engine/archive/refs/tags/0.1.tar.gz",   
  keywords = ['LLM', 'gorilla', 'execution engine'],

#   classifiers=[
#     'Development Status :: 3 - Alpha',      
#     'Intended Audience :: Developers',      
#     'Topic :: Software Development :: Build Tools',
#     'License :: OSI Approved :: MIT License',
#     'Programming Language :: Python :: 3',   
#     'Programming Language :: Python :: 3.4',
#     'Programming Language :: Python :: 3.5',
#     'Programming Language :: Python :: 3.6',
#   ],
)

# setup(
#     name='gorilla-x',
#     version='1.0.0',
#     url="https://github.com/gorilla-llm/exec-engine",
#     packages=find_packages(),
#     author="Shishir Patil, Noppapon Chalermchockcharoenkit, Roy Huang, Liheng Lai, Aaron Hao",
#     description="CLI for Gorilla Execution Engine",
#     entry_points={
#         'console_scripts': [
#             'gorilla-x = cli:main'
#         ],
#     }
# )
