from conan import ConanFile
from conan.tools.scm import Git


class ConanRecipe(ConanFile):
    name = "conan-grafted"
    version = "1.2.3"

    def export(self):
        git = Git(self, self.recipe_folder)
        git.coordinates_to_conandata(repository=True)
