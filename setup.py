from setuptools import find_packages , setup


def get_requriments(path:str) -> list[str]:
    
    requriments = []
    with open(path) as requriment_file:
        for req in requriments:
            req =  req.strip()
            if req and req != '-e .':
                requriments.append(req)
                
    return requriments

setup(
    
    name = "my_package",
    version='0.1',
    author='Krishna',
    author_email='saik36048@gmail.com',
    description='MLops end to end project',
    packages= find_packages(),
    install_requires=get_requriments('requriment.txt')
    
    )