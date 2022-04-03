 from Py.Inspeccion import Inspeccion
 from Py.Vehiculo import vehiculo
 from Py.Persona import persona
 from Py.Tipo_Revision import Tipo_Revision
 from Py.Revision import Revision
 from Conf.ConfBd import mySQLdb, dbData
 from flask import Flask
 from flas_restful import Api


app= Flask(__name__)
api=Api(app)


 app.config['MYSQL_HOST'] = dbData['host']
 app.config['MYSQL_USER'] = dbData['user']
 app.config['MYSQL_PASSWORD'] = dbData['pass']
 app.config['MYSQL_DB'] = dbData['dataBase']

 mySQLdb.init_app(app)


 api.add_resource(persona,'/Persona','/Persona/<id>')
 api.add_resource(Inspeccion,'/Inspeccion','/Inspeccion/<id>')
 api.add_resource(Revision,'/Revision','/Revision/<id>')
 api.add_resource(Tipo_Revision,'/TipoRevision','/TipoRevision/<id>')



 if  __name__=="__main__":
    app.run(debug=True)




#  @app.route("/")
# def index():
#     return "hola"

# if  __name__=="__main__":
#     app.run(debug=True)
