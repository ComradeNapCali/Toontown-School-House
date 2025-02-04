# -------------------------------------------------------------------------------
# Contact: Mark Wojtowicz
# Created: June 2010
# -------------------------------------------------------------------------------

from toontown.parties.DistributedPartyTrampolineActivity import DistributedPartyTrampolineActivity
from toontown.parties import PartyGlobals

class DistributedPartyVictoryTrampolineActivity(DistributedPartyTrampolineActivity):
    """ Reskinned trampoline for victory party holiday. """

    def __init__(self, cr, doJellyBeans=True, doTricks=False, texture=None):
        self.notify.debug("Intializing.")
        DistributedPartyTrampolineActivity.__init__(self,
                                                    cr,
                                                    doJellyBeans,
                                                    doTricks,
                                                    "phase_13/maps/tt_t_ara_pty_trampolineVictory.jpg",
                                                    activityId=PartyGlobals.ActivityIds.PartyVictoryTrampoline
                                                    )
