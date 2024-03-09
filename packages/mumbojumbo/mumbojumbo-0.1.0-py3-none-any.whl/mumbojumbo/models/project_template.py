# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#   Copyright 2024 Patrick Hohenecker                                         #
#                                                                             #
#   Redistribution and use in source and binary forms, with or without        #
#   modification, are permitted provided that the following conditions        #
#   are met:                                                                  #
#                                                                             #
#   1. Redistributions of source code must retain the above copyright         #
#      notice, this list of conditions and the following disclaimer.          #
#                                                                             #
#   2. Redistributions in binary form must reproduce the above copyright      #
#      notice, this list of conditions and the following disclaimer in the    #
#      documentation and/or other materials provided with the distribution.   #
#                                                                             #
#   3. Neither the name of the copyright holder nor the names of its          #
#      contributors may be used to endorse or promote products derived        #
#      from this software without specific prior written permission.          #
#                                                                             #
#   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS       #
#   “AS IS” AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT         #
#   LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR     #
#   A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT      #
#   HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,    #
#   SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT          #
#   LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,     #
#   DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY     #
#   THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT       #
#   (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE     #
#   OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.      #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


import pathlib

import mumbojumbo.models.template_variable as template_variable

from dataclasses import dataclass


@dataclass
class ProjectTemplate:
    """Describes a single project template (consisting of possibly multiple files).

    A :class:`~.ProjectTemplate` is simply a directory containing an arbitrary number of subdirectories and files that
    serve as a stencil for generating the boilerplate structure of new projects. The root directory of a
    :class:`~.ProjectTemplate` is stored as :attr:`~.ProjectTemplate.template_dir`, and the paths (relative to the
    :attr:`~.ProjectTemplate.template_dir`) of all files considered part of the :class:`~.ProjectTemplate` are listed as
    the :attr:`~.ProjectTemplate.template_files`. Notice that subdirectories are not explicitly stored, but are
    implicitly defined by the :attr:`~.ProjectTemplate.template_files`. The reason why
    :attr:`~.ProjectTemplate.template_files` are explicitly defined as opposed to using "everything" in the
    :attr:`~.ProjectTemplate.template_dir` is that this allows for excluding certain special/system files (e.g., the
    ``.DS_Store`` files on Mac).

    An important aspect of :class:`~.ProjectTemplate`\\ s are the :attr:`~.ProjectTemplate.custom_variables`, which
    define all the configurable parameters of a :class:`~.ProjectTemplate`. Whenever a :class:`~.ProjectTemplate` is
    applied (by means of :ref:`mj-apply <mj-apply>`), the user is prompted to provide values for these
    :attr:`~.ProjectTemplate.custom_variables`, and the specified custom values are then provided to the
    :class:`~mumbojumbo.template_renderer.TemplateRenderer` that actually generates the new project directory based on
    the used :class:`~.ProjectTemplate`.

    Note:
        The :attr:`~.ProjectTemplate.template_dir` of every :class:`~.ProjectTemplate` has to contain a special file
        called ``template.json``, which defines the details of the template (other than the
        :attr:`~.ProjectTemplate.template_files`) and which is **not** part of the
        :attr:`~.ProjectTemplate.template_files`. Confer the documentation of the
        :class:`~mumbojumbo.template_loader.TemplateLoader` for all details.
    """

    #  ATTRIBUTES  #####################################################################################################

    name: str
    """The name of the :class:`~.ProjectTemplate`."""

    description: str
    """A description of the :class:`~.ProjectTemplate`. This is displayed to users when they list all templates."""

    template_dir: pathlib.Path
    """The path of the directory that contains all files that are part of the :class:`~.ProjectTemplate`."""

    template_files: list[pathlib.Path]
    """The paths (relative to the :attr:`~.ProjectTemplate.template_dir`) of all files that are part of the
    :class:`~.ProjectTemplate`.
    """

    custom_variables: list[template_variable.TemplateVariable]
    """All custom variables used by the :class:`~.ProjectTemplate`."""

    #  METHODS  ########################################################################################################

    @staticmethod
    def _parse_template_variables(variables_as_json: list[dict[str, str]]) -> list[template_variable.TemplateVariable]:
        """Parses the given ``variables_as_json`` into the according :class:`~.template_variable.TemplateVariables`\\ s.
        """

        return [template_variable.TemplateVariable.from_json(x) for x in variables_as_json]

    @classmethod
    def create(
            cls,
            template_dir: pathlib.Path,
            template_files: list[pathlib.Path],
            template_json: dict
    ) -> "ProjectTemplate":
        """Creates a :class:`~.ProjectTemplate` based on the provided details.

        Args:
            template_dir: The :class:`~pathlib.Path` of the directory that contains the created
                :class:`~.ProjectTemplate`.
            template_files: The :class:`~pathlib.Path`\\ s (relative to the ``template_dir``) of all files that are part
                of the :class:`~.ProjectTemplate`.
            template_json: The ``template.json`` file located in the ``template_dir``.
        """

        custom_variables = (
                cls._parse_template_variables(template_json["custom_variables"])
                if "custom_variables" in template_json else
                []
        )
        return ProjectTemplate(
                template_json["name"],
                template_json["description"],
                template_dir,
                template_files,
                custom_variables
        )
