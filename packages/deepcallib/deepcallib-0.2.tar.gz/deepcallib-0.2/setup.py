from setuptools import setup

setup(
    name='deepcallib',
    version='0.2',
    packages=['deepcallib'],
    install_requires=[
        # List your dependencies here
    ],
    license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description = 'ML speedup for Vam Tool Box projection generation',   # Give a short description about your library
    author = 'Mark Ogata',                   # Type in your name
    author_email = 'ogata@berkeley.edu',      # Type in your E-Mail
    url = 'https://github.com/Clamepending/deepCAL/tree/tweaking_ML',   # Provide either the link to your github or to your website
    
    keywords = ['CAL', 'vamtoolbox'],   # Keywords that define your package best
    classifiers=[
        'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        'Programming Language :: Python :: 3.9',      #Specify which pyhton versions that you want to support
        
    ],
)