Tests using Boost, Conan and MinGW

# Instructions

Enter the ConanMinGW directory and run the following:

    > cd ConanMinGW
    > conan install
    > activate
    > cd ..\Recreate
    > mkdir build
    > cd build
    > conan install .. -s compiler=gcc -s compiler.libcxx=libstdc++11 -s compiler.version=4.9
    > conan build ..

