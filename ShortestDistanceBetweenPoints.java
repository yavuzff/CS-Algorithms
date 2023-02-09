import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

//good version (below): T(n) = O(nlogn) + P(n), P(n) = 2P(n/2) + O(n)
public class ShortestDistanceBetweenPoints {
    public static double findclosest(ArrayList<Point> points){
        ArrayList<Point> xsorted = new ArrayList<Point>(points);
        Collections.sort(xsorted,((o1, o2) -> {
            if (o1.x < o2.x){
                return -1;
            }
            else {
                return 1;
            }
        }));

        ArrayList<Point> ysorted = new ArrayList<Point>(points);
        Collections.sort(xsorted,((o1, o2) -> {
            if (o1.y < o2.y){
                return -1;
            }
            else {
                return 1;
            }
        }));

        return helper(xsorted,ysorted);
    }

    private static double helper (ArrayList<Point> xsorted,ArrayList<Point> ysorted){
        if (xsorted.size() == 2){
            return Point.distance(xsorted.get(0),xsorted.get(1));
        }
        if (xsorted.size() < 2 ){
            return Double.POSITIVE_INFINITY;
        }

        int mid = xsorted.size() / 2;
        ArrayList<Point> xleft = new ArrayList<Point>(xsorted.subList(0,mid));
        ArrayList<Point> xright = new ArrayList<Point>(xsorted.subList(mid,xsorted.size()));

        double middle = (xleft.get(mid-1).x + xright.get(0).x)/2;
        ArrayList<Point> yleft = new ArrayList<>();
        ArrayList<Point> yright = new ArrayList<>();

        //produce sorted yleft and yright O(n)
        for (Point p: ysorted){
            if (p.x < middle){
                yleft.add(p);
            }
            else{
                yright.add(p);
            }
        }

        double closest_left = helper(xleft,yleft);
        double closest_right = helper(xright,yright);
        double m = Math.min(closest_left,closest_right);
        //above has the shortest distance for each of the halves
        //however, there could be two points in opposite halves with distance less than m

        //remove elements from the points that are more than m away from the center - these simply cannot be
        //This step is O(n) - could result in all points still being in, e.g. if we had two vertical dotted lines
        ArrayList<Point> temp = new ArrayList<>();
        for (Point p: ysorted){
            if (middle - m <= p.x && p.x <=middle + m){ // point is within d of boundary
                temp.add(p); //consider point
            }
        }

        //important point: given a point, any point with y-value further than 7 points must be more than m away.
        //if the 8th point was distance m away, then there must exist some points that had less than distance m and are on the same side
        //this occurs since an mxm square can contain at most 4 points.

        //O(n)
        for (int i = 0; i<temp.size(); i++){
            for (int j = i+1; j<Math.min(temp.size(),i+8); j++){
                Point p1 = temp.get(i);
                Point p2 = temp.get(j);
                double d = Point.distance(p1,p2);
                if (d<m){
                    m = d;
                }
            }
        }

        return m;
    }
}
