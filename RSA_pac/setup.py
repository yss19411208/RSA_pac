from setuptools import setup, find_packages

def get_requirements_from_file():
    with open("./requirements.txt") as f_in:
        requirements = f_in.read().splitlines()
    return requirements

setup(
    name='RSA_pac',  # パッケージ名（pip listで表示される）
    version="0.0.1",  # バージョン
    description="make a RSA",  # 説明
    author='yss19411208',  # 作者名
    packages=find_packages(),  # 使うモジュール一覧を指定する
    license='MIT',  # ライセンス
    install_requires=get_requirements_from_file()
)