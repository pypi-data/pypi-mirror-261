cmake -B /opt/cc/ -S cppsrc/core -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/opt/cc/install
make -C /opt/cc/ install -j

cd /opt
mkdir main
cd main
cmake -B /opt/main -S /workspace/cppsrc/main -DCMAKE_BUILD_TYPE=Release -DCMAKE_PREFIX_PATH=/opt/cc/install -DCMAKE_INSTALL_PREFIX=/opt/main/install
make -C /opt/main install -j

LD_LIBRARY_PATH=/opt/cc/install/lib
/opt/main/install/bin/coverage_algorithm
