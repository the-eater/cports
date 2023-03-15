import pathlib

from cbuild.core.template import Template


class Zig:
    def __init__(self, tmpl: Template, env={}, wrksrc=None):
        self.template = tmpl
        self.wrksrc = wrksrc
        self.env = env

    def build(self):
        self.template.do(
            "zig", "build", "-Dpie", "--prefix", "/usr", "-Dcpu=baseline", *self.template.make_build_args, "install",
            env={
                "DESTDIR": "zig-out"
            }
        )

    def check(self):
        self.template.do("zig", "build", "-Dpie", "--prefix", "/usr", "-Dcpu=baseline", *self.template.make_build_args,
                         "test")

    def install(self):
        tmpl = self.template

        output: pathlib.Path = tmpl.cwd / "zig-out"
        # I don't think there's an easier way to simulate mv $DIR/* $DEST/
        for item in output.iterdir():
            tmpl.mv(item, tmpl.destdir)
