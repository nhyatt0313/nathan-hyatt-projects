package storymaps.dao;

import java.util.List;

public interface Trait {
    List<Trait> getTraitsByCharacterId(int characterId);

    Trait crateTrait(Trait trait);
    Trait readTrait(int id);
    Trait updateTrait(Trait trait);
    Trait deleteTrait(int id);
}
