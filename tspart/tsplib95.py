# Exports
__all__ = ['tsplib95']


class tsplib95:

    @classmethod
    def export_problem(cls, filename, nodes, name='tsp-art', comment='Created with tsp-art library for Python'):
        with open(filename, 'w') as f:
            f.write(f'NAME: {name}\n')
            f.write(f'TYPE: TSP\n')
            f.write(f'COMMENT: {comment}\n')
            f.write(f'DIMENSION: {len(nodes)}\n')
            f.write(f'EDGE_WEIGHT_TYPE: EUC_2D\n')

            f.write(f'NODE_COORD_SECTION\n')
            for i in range(0, len(nodes)):
                f.write(f'{i + 1} {nodes[i][0]} {nodes[i][1]}\n')

            f.write(f'EOF\n')

    @classmethod
    def export_tour(cls, filename, tour, name='tsp-art', length=None, comment=None):
        with open(filename, 'w') as f:
            f.write(f'NAME: {name}\n')

            if length is not None:
                f.write(f'COMMENT: length = {length}\n')

            if comment is not None:
                f.write(f'COMMENT: {comment}\n')

            f.write(f'TYPE: TOUR\n')
            f.write(f'DIMENSION: {len(tour)}\n')

            f.write(f'TOUR_SECTION\n')
            for i in tour:
                f.write(f'{i + 1}\n')

            f.write(f'-1\n')
            f.write(f'EOF\n')

    @classmethod
    def load_tour(cls, filename):

        # Load file content to a string
        data = None
        with open(filename, 'r') as f:
            data = f.readlines()

        # Get tour dimension
        n = None
        for line in data:
            tokens = [token.strip() for token in line.split(':')]
            if tokens[0].upper() == 'DIMENSION':
                n = int(tokens[1])
                break

        # Find first line of tour section
        idx = 0
        for line in data:
            tokens = [token.strip() for token in line.split(':')]
            if tokens[0].upper() == 'TOUR_SECTION':
                idx = idx + 1
                break
            else:
                idx = idx + 1

        # Load tour as a list
        tour = [int(line.strip()) - 1 for line in data[idx:(idx + n)]]
        return tour
