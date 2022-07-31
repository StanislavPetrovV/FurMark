import moderngl_window as mglw


class App(mglw.WindowConfig):
    window_size = 1600, 900
    resource_dir = 'resources'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.quad = mglw.geometry.quad_fs()
        self.program = self.load_program(vertex_shader='programs/vertex.glsl',
                                         fragment_shader='programs/fragment.glsl')
        self.set_uniform('u_resolution', self.window_size)

        self.texture1 = self.load_texture_2d('textures/fur.jpg')
        self.set_uniform('u_texture1', 1)
        self.texture1.use(location=1)

        self.texture2 = self.load_texture_2d('textures/noise.png')
        self.set_uniform('u_texture2', 2)
        self.texture2.use(location=2)

        self.texture3 = self.load_texture_2d('textures/wall.jpg')
        self.set_uniform('u_texture3', 3)
        self.texture3.use(location=3)

    def set_uniform(self, u_name, u_value):
        try:
            self.program[u_name] = u_value
        except KeyError:
            print(f'{u_name} not used in shader')

    def render(self, time, frame_time):
        self.ctx.clear()
        self.set_uniform('u_time', time)
        self.quad.render(self.program)


if __name__ == '__main__':
    mglw.run_window_config(App)
