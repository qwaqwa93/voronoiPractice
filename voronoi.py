from PIL import Image, ImageDraw
import sys
import random
import math
import heapq

def gen_random_points(n, length, height):
    points = []
    for i in range(int(n)):
        x = random.randrange(0, length)
        y = random.randrange(0, height)
        points.append((x, y))
    return points

def gen_voronoi_graph(points, length, height):
    
    return

def gen_voronoi_image(graph, points, init_image):
    im = init_image
    return image

# gen_voronoi_image_brute : points, image => image
# For each pixels, find nearest point among the given points by comparing 
# all points and set its color same as that point
def gen_voronoi_image_brute(points, image):
    voronoi_image = image.copy()
    draw = ImageDraw.Draw(voronoi_image) 
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            draw.point((i, j), fill=im.getpixel(nearest_point((i, j), points)))
        # (Optional) indicate given points with red color
        #for point in points:
        #    draw.point(point, fill="#ff0000")
    del draw
    return voronoi_image

def dist(p1, p2):
    return math.sqrt(math.pow(p1[0] - p2[0], 2) + math.pow(p1[1] - p2[1], 2))

def nearest_point(target_point, points):
    min_dist = dist(target_point, points[0])
    nearest_point = points[0]
    for point in points:
        cur_dist = dist(target_point, point)
        if min_dist > cur_dist:
            min_dist = cur_dist
            nearest_point = point
    return nearest_point

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "Usage: $ python voronoi.py [target Image] [# of points]"
        exit()
    im = Image.open(sys.argv[1])
    num_points = sys.argv[2]
    points = gen_random_points(num_points, im.size[0], im.size[1])
    
    """
    # Test gen_random_points
    draw = ImageDraw.Draw(im)
    draw.point(points, fill="#ff0000")
    del draw
    im.show()
    """

    # Test gen_voronoi_image_brute
    vornonoi_image = gen_voronoi_image_brute(points, im)
    im.show()
    vornonoi_image.show()
    
