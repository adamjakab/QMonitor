import cherrypy


class Root(object):
    @cherrypy.expose
    def index(self):
        cherrypy.log("INDEX HIT!")
        return "Index page"

class Monitor(object):
    @cherrypy.expose
    def index(self):
        return "Monitor"

class Configuration(object):
    @cherrypy.expose
    def index(self):
        return "Configuration"
    
    # http://127.0.0.1:8080/configuration/test_me_too
    @cherrypy.expose(alias="test_me_too")
    def test_me(self):
        return "Configuration2"



if __name__ == '__main__':
    # Global Configuration
    cherrypy.config.update( 
        {
            'log.screen': True,
            'log.access_file': '',
            'log.error_file': ''
        }
    )

    # App Configuration
    conf = {}
    conf_root = {}
    conf_monitor = {}
    conf_configuration = {}

    # Mount Applications
    cherrypy.tree.mount(Root(), '/', conf_root)
    cherrypy.tree.mount(Monitor(), '/monitor', conf_monitor)
    cherrypy.tree.mount(Configuration(), '/configuration')

    # Run the engine
    cherrypy.engine.start()
    cherrypy.engine.block()


