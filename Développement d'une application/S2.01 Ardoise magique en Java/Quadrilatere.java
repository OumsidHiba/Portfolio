import ardoise.Forme;
import ardoise.PointPlan;
import ardoise.Segment;

import java.util.ArrayList;

public class Quadrilatere extends Forme {
    private PointPlan point1;
    private PointPlan point2;
    private PointPlan point3;
    private PointPlan point4;

    public Quadrilatere(String nomForme, PointPlan point1, PointPlan point2, PointPlan point3, PointPlan point4) {
        super(nomForme);
        this.point1 = point1;
        this.point2 = point2;
        this.point3 = point3;
        this.point4 = point4;
    }

    @Override
    public void deplacer(int deplacementX, int deplacementY) {
        point1.deplacer(deplacementX, deplacementY);
        point2.deplacer(deplacementX, deplacementY);
        point3.deplacer(deplacementX, deplacementY);
        point4.deplacer(deplacementX, deplacementY);
    }

    @Override
    public ArrayList<Segment> dessiner() {
        ArrayList<Segment> segments = new ArrayList<>();
        segments.add(new Segment(point1, point2));
        segments.add(new Segment(point2, point3));
        segments.add(new Segment(point3, point4));
        segments.add(new Segment(point4, point1));
        return segments;
    }

    @Override
    public String typeForme() {
        return "Q";
    }
}
