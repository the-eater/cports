from cbuild.util.zig import Zig


def do_check(self):
    self.zig.check()


def do_install(self):
    self.zig.install()


def do_build(self):
    self.zig.build()


def use(tmpl):
    tmpl.do_build = do_build
    tmpl.do_install = do_install
    tmpl.do_check = do_check

    tmpl.zig = Zig(tmpl)
