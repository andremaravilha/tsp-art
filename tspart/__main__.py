import argparse
import tspart


def main():

    # Parse command line input arguments
    parser = argparse.ArgumentParser(description='TSP Art')
    parser.add_argument('file_input', metavar='PATH', type=str,
                        help='Path to input image file.')
    parser.add_argument('file_output', metavar='OUTPUT', type=str,
                        help='Name to the output image file. Supported formats are PNG, PDF, EPS, SVG.')
    parser.add_argument('--nodes', dest='nodes', metavar='N', type=int, default=None,
                        help='Maximum number of nodes for the TSP.')
    parser.add_argument('--solver', dest='solver', metavar='NAME', type=str, default='lkh',
                        help='TSP solver: lkh')
    parser.add_argument('--draw-instance', dest='draw_instance', metavar='FILE', type=str, default=None,
                        help='Create an image with nodes from the resulting TSP instance. Supported formats are PNG, '
                             'PDF, EPS, SVG.')
    parser.add_argument('--export-instance', dest='export_instance', metavar='FILE', type=str, default=None,
                        help='Export the resulting TSP instance to TSPLIB format.')
    parser.add_argument('--export-tour', dest='export_tour', metavar='FILE', type=str, default=None,
                        help='Export the tour to TSPLIB format.')

    args = parser.parse_args()

    # Step 1: Get a TSP instance (list of nodes, i.e., <x,y>-coordinates) from input image
    nodes = tspart.extract_nodes(args.file_input, n=args.nodes)

    if args.export_instance is not None:
        tspart.tsplib95.export_problem(args.export_instance, nodes)

    if args.draw_instance is not None:
        tspart.draw_nodes(args.draw_instance, nodes)

    # Step 2: Solve TSP instance and get the best tour found
    tour = tspart.solve_tsp(nodes, solver=args.solver)

    if args.export_tour is not None:
        tspart.tsplib95.export_tour(args.export_tour, tour)

    # Step 3: Draw the TSP tour
    tspart.draw_tour(args.file_output, tour, nodes)


if __name__ == '__main__':
    main()
