import os
import sys
import tempfile
import subprocess
from ..tsplib95 import tsplib95

# Exports
__all__ = ['linkernighan']


def linkernighan(nodes):

    # Solver path
    solver_path = 'LKH'
    if sys.platform == 'win32':
        from importlib.resources import path as resource_path
        from .. import bin
        with resource_path(bin, 'LKH-3.exe') as p:
            solver_path = os.path.abspath(str(p))

    # Temporary files
    problem_file = os.path.join(tempfile.gettempdir(), os.urandom(24).hex())
    tour_file = os.path.join(tempfile.gettempdir(), os.urandom(24).hex())
    params_file = os.path.join(tempfile.gettempdir(), os.urandom(24).hex())

    # Create file with parameters to the LKH executable
    with open(params_file, 'w') as f:
        f.write(f'PROBLEM_FILE = {problem_file}\n')
        f.write(f'TOUR_FILE = {tour_file}\n')
        f.write(f'INITIAL_TOUR_ALGORITHM = QUICK-BORUVKA\n')
        f.write(f'RUNS = 1\n')
        f.write(f'TRACE_LEVEL = 0\n')
        f.write(f'EOF\n')

    # Create the temporary file with problem data in TSPLIB format
    tsplib95.export_problem(problem_file, nodes)

    # Run LKH
    try:
        subprocess.check_output([solver_path, params_file], stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        raise Exception(e.output.decode())

    # Read solution from file
    tour = tsplib95.load_tour(tour_file)

    # Delete temporary files
    os.unlink(tour_file)
    os.unlink(problem_file)
    os.unlink(params_file)

    return tour
