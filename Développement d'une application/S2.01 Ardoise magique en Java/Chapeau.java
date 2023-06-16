import ardoise.Forme;
import ardoise.PointPlan;
import ardoise.Segment;

import java.util.ArrayList;

public class Chapeau extends Forme {
    private PointPlan point1;
    private PointPlan point2;
    private PointPlan point3;

    public Chapeau(String nomForme, PointPlan point1, PointPlan point2, PointPlan point3) {
        super(nomForme);
        this.point1 = point1;
        this.point2 = point2;
        this.point3 = point3;
    }

    @Override
    public void deplacer(int deplacementX, int deplacementY) {
        point1.deplacer(deplacementX, deplacementY);
        point2.deplacer(deplacementX, deplacementY);
        point3.deplacer(deplacementX, deplacementY);
    }

    @Override
    public ArrayList<Segment> dessiner() {
        ArrayList<Segment> segments = new ArrayList<>();
        segments.add(new Segment(point1, point2));
        segments.add(new Segment(point2, point3));
        return segments;
    }

    @Override
    public String typeForme() {
        return "C";
    }
}
