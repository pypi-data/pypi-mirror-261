from distutils.core import setup
setup(
  name = 'rvs_palmvision',         # How you named your package folder (MyLib)
  packages = ['rvs_palmvision'],   # Chose the same as "name"
  version = '0.0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Machine Learning using Palmvision ! ',   # Give a short description about your library
  author = 'Rohith Vijay R',                   # Type in your name
  author_email = 'rohithvijayr6012@gmail.com',      # Type in your E-Mail
  #url = 'https://github.com/user/reponame',   # Provide either the link to your github or to your website
  #download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['Computervisiom', 'Machine Learning', 'handtracking','palmvision'],   
  install_requires=[            
          'opencv_python',
          'mediapipe',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      

    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',

    'License :: OSI Approved :: MIT License',   

    'Programming Language :: Python :: 3.6',      
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.12',
  ],
)