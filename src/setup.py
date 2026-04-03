from setuptools import setup
import setup_translate

pkg = 'Extensions.EPGRefresh'
setup(name='enigma2-plugin-extensions-epgrefresh',
       version='3.0',
       description='Plugin to refresh EPG Data when Receiver is inactive',
       package_dir={pkg: 'EPGRefresh'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', 'mphelp.xml', 'LICENSE', 'EPGRefresh.png', 'localehelp/de/mphelp.xml', 'localehelp/fi/mphelp.xml', 'localehelp/it/mphelp.xml', 'localehelp/pt/mphelp.xml']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
