#%Module

# Automatically determined name and version
set name [file dirname [module-info name]]
set version [file tail [module-info name]]

# FIXME: Update this line with a description of the software
set description "description of software goes here"
# FIXME: Update the project name/location of the modules
set root /projects/my-project/apps/modules/software/${name}/${version}

proc ModulesHelp { } {
   global name version
   puts stderr "\tLoads the ${name} version ${version} environment"
   puts stderr "\n\tFor further information, use 'module display [module-info name]'"
}

proc ModulesDisplay { } {
   global description
   puts stderr "\n${description}"
}

module-whatis "${name} [file tail [module-info name]] - ${description}"

# FIXME: Update/add environment variables required by the software
prepend-path PATH ${root}/bin
