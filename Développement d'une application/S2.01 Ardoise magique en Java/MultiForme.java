import ardoise.Forme;
import ardoise.PointPlan;
import ardoise.Segment;

import java.util.ArrayList;
import java.util.List;

public class MultiForme extends Forme {
    private List<Forme> formes;

    public MultiForme(String nomForme, Forme... formes) {
        super(nomForme);
        this.formes = new ArrayList<>();
        for (Forme forme : formes) {
            this.formes.add(forme);
        }
    }

    @Override
    public void deplacer(int deplacementX, int deplacementY) {
        for (Forme forme : formes) {
            forme.deplacer(deplacementX, deplacementY);
        }
    }

    @Override
    public ArrayList<Segment> dessiner() {
        ArrayList<Segment> segments = new ArrayList<>();
        for (Forme forme : formes) {
            segments.addAll(forme.dessiner());
        }
        return segments;
    }

    @Override
    public String typeForme() {
        return "GF";
    }
}
