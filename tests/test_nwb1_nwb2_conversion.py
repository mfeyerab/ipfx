import os
import pytest

from ipfx.x_to_nwb.NWBConverter import NWBConverter
from .helpers_for_tests import diff_h5, validate_nwb
from ipfx.bin.run_nwb1_to_nwb2_conversion import make_nwb2_file_name
from hdmf import Container


class TestNWBConverter(NWBConverter):

    @staticmethod
    def undefined_object_id(self):
        """
        Monkey patching object_id property to set to a fixed value. overriding
        Reassigning Container.object_id is needed for regression testing because
        object_id is unique to created object rather than to data.

        Parameters
        ----------
        self

        Returns
        -------

        """
        return "Undefined"

    def __init__(self, input_file, output_file):

        Container.object_id = property(self.undefined_object_id)

        NWBConverter.__init__(self, input_file, output_file)




@pytest.mark.parametrize('NWB_file_inhouse', ['Pvalb-IRES-Cre;Ai14-406663.04.01.01.nwb',
                                              'H18.03.315.11.11.01.05.nwb'], indirect=True)
def test_file_level_regressions(NWB_file_inhouse,tmpdir_factory):

    nwb1_file_name = NWB_file_inhouse
    base_name = os.path.basename(nwb1_file_name)

    test_dir = os.path.dirname(nwb1_file_name)
    test_nwb2_file_name = make_nwb2_file_name(test_dir,base_name)

    temp_dir = str(tmpdir_factory.mktemp("nwb_conversions"))
    temp_nwb2_file_name = make_nwb2_file_name(temp_dir,base_name)

    assert os.path.isfile(nwb1_file_name)
    assert os.path.isfile(test_nwb2_file_name)

    TestNWBConverter(input_file=nwb1_file_name,
                     output_file=temp_nwb2_file_name,
                     )

    assert validate_nwb(temp_nwb2_file_name) == []
    assert diff_h5(temp_nwb2_file_name,test_nwb2_file_name) == 0


