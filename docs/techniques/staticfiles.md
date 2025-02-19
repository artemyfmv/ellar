# **Static Files**
A static file is a type of file that does not change often and is not generated by a server-side script. Examples of static files include images, CSS and JavaScript files, audio and video files, and other types of media.

Static files in Ellar are served using the `StaticFiles` ASGI class, which is an extension of the Starlette `StaticFiles` ASGI class. 
This class uses the static files specified in the application's **modules** and **configuration**.

In addition, Ellar creates a route that mounts the static server at the `/static` path. 
The path can be modified by providing a new value for the `STATIC_MOUNT_PATH` configuration variable.

## **Configuring static files**

1. In your config file, define `STATIC_MOUNT_PATH`, for example:
    ```python
    class Config:
        STATIC_MOUNT_PATH = '/static'
    ```

2. Store your static files in a folder called **static** in your module. For example **my_module/static/my_module/example.jpg**.
3. In your templates, use the `url_for` with `static` and `path` parameter to build the URL for the given relative path using the configured in `STATIC_DIRECTORIES`, `STATIC_FOLDER_PACKAGES` or Module.
   ```html
    <img src="{{url_for('static', path='my_module/example.jpg')}}" alt="My image">
   ```
   OR, visit `/static/my_app/example.jpg`


## **Static File in Modules**

Managing multiple sets of static files in larger projects can be challenging, 
but by organizing each set of static files within a specific module, 
it becomes easier to manage and maintain. 
This approach allows for clear organization and separation of static assets, 
making it more manageable in a large project.

In our previous project, within the `car` module folder, we can create a following directories, `my_static/car`. 
Inside this folder `my_static/car`, we can create a file named `example.txt`. 
This allows us to keep all of the static files related to the car module organized in one location `my_static`.

Next, we tell `CarModule` about our static folder.

```python
# project_name/apps/car/module.py

from ellar.common import Module
from ellar.core import ModuleBase
from ellar.di import Container

from .controllers import CarController


@Module(
    controllers=[CarController], static_folder='my_static'
)
class CarModule(ModuleBase):
    def register_providers(self, container: Container) -> None:
        # for more complicated provider registrations
        # container.register_instance(...)
        pass
```

## **Other Static Configurations**
In addition to setting static directories within modules, 
it is also possible to manually specify additional static directories that are not located within a module by using the 
`STATIC_FOLDER_PACKAGES` and `STATIC_DIRECTORIES` variables in the application's configuration. 
These variables allow for even more flexibility in organizing and managing static files in a project. 
These directories will be served by the StaticFiles ASGI class along with the module-scoped static files.

### **`STATIC_DIRECTORIES`**
`STATIC_DIRECTORIES` variable is a list of directories within the project that contain static files. 
These directories are not necessarily scoped to a specific module and can be used to serve static files from any location within the project. 
These directories can be added to the `STATIC_DIRECTORIES` list in the application's configuration.

```python
STATIC_DIRECTORIES =  ['project_name/static-files', 'project_name/path/to/static/files']
```

### **`STATIC_FOLDER_PACKAGES`**
`STATIC_FOLDER_PACKAGES` variable is a list of tuples that contain python packages that hold some static files. 
These packages should have a `static` folder and the **package name** should be passed as tuple `(package_name, package_path)`, 
**package_path** is the relative path of static folder.

```python

STATIC_FOLDER_PACKAGES =  [('bootstrap', 'statics'), ('package-name', 'path/to/static/directory')]
```

Static files will respond with "404 Not found" or "405 Method not allowed" responses for requests which do not match. In `HTML` mode if `404.html` file exists it will be shown as 404 response.
