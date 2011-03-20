from setuptools import setup, find_packages
import os
import platform

DESCRIPTION = "Convenient helper to send multipart/alternative or regular email based on templates."

LONG_DESCRIPTION = None
try:
    LONG_DESCRIPTION = open('README.rst').read()
except:
    pass

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Framework :: Django',
]

setup(
    name='django-email-templates',
    version='0.1',
    packages=['email_templates'],
    author=u'S\xe6var \xd6fj\xf6r\xf0 Magn\xfasson',
    author_email='saevar@saevar.is',
    url='http://github.com/saevarom/django-email-templates',
    license='MIT',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    platforms=['any'],
    classifiers=CLASSIFIERS,
)
