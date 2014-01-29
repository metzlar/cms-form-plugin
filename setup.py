from setuptools import setup

setup(
    name='cms-form-plugin',
    version=".".join(map(str, __import__('cms_form_plugin').__version__)),
    packages=['cms_form_plugin', 'cms_form_plugin.migrations'],
    package_dir={'cms_form_plugin': 'cms_form_plugin'},
    package_data={'cms_form_plugin': ['templates/*/*']},
    install_requires=[
        'django',
        'django-cms'
    ],
    url='https://www.github.com/metzlar/cms-form-plugin',
    license=open('LICENSE').read(),
    author='Ivan Metzlar',
    author_email='metzlar@gmail.com',
    description='Django CMS Form plugin inspired by django.views.generic.edit.FormView',
    long_description=open('README.md').read(),
    keywords=[
        'django',
        'django-cms',
        'web',
        'cms',
        'cmsplugin',
        'plugin',
    ],
    platforms='OS Independent',
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Programming Language :: Python',
        'Framework :: Django',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development'
    ],
)