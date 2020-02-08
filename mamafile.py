import mama
class curl(mama.BuildTarget):
    def dependencies(self):
        pass

    def configure(self):
        self.add_cmake_options('BUILD_CURL_EXE=OFF', 'BUILD_TESTING=OFF',
                               'CURL_STATICLIB=ON', 'CURL_STATIC_CRT=ON',
                               'CURL_DISABLE_LDAP=ON', 'CURL_DISABLE_LDAPS=ON',
                               'CMAKE_USE_OPENSSL=OFF', 'CURL_CA_BUNDLE=none',
                               'CURL_CA_PATH=none')

    def package(self):
        self.copy_built_file('lib/curl_config.h', 'include/curl')
        self.export_include('include', build_dir=True)
        self.export_libs('lib', ['libcurl.lib', '.a'])
        if self.windows:
            self.export_syslib('Ws2_32.lib')
        if self.linux:
            self.export_syslib('z')
