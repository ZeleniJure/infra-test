''' Arch type map for GOARCH '''
ARCH_TYPE = dict(
    x86_64="amd64",
    aarch64="arm64",
)


def to_go_arch(architecture):
    ''' Switch architecture to GOARCH '''

    return ARCH_TYPE.get(architecture, architecture)


class FilterModule(object):
    def filters(self):
        return {'to_go_arch': to_go_arch}
