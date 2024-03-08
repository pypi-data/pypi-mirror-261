pip install . -v

cd /opt
mkdir main
cd main
cmake -B /opt/main -S /workspace/cppsrc/main -DCMAKE_BUILD_TYPE=Release -DCMAKE_PREFIX_PATH=/opt/venv/lib/python3.10/site-packages/test_coverage -DCMAKE_INSTALL_PREFIX=/opt/main/install
make -C /opt/main install -j

LD_LIBRARY_PATH=/opt/venv/lib/python3.10/site-packages/test_coverage/lib
/opt/main/install/bin/coverage_algorithm

