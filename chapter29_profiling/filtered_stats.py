import pstats

def formatted_stats_output(path):
    p = pstats.Stats(path)
    stripped_dirs = p.strip_dirs()
    sorted_stats = stripped_dirs.sort_stats('filename')
    sorted_stats.print_stats('\(main')

if __name__ =='__main__':
    path = 'profile_output.txt'
    formatted_stats_output(path)