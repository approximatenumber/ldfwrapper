import ldfparser

class LDFWrapper():
    def __init__(self, ldf_file: str) -> None:
        """Constructor."""
        self.ldf_file = None
        self._parsed_data = self._get_parsed_ldf_file(ldf_file)
        self.signals = self._get_signals()
        self.frames = self._get_frames()

    def _get_parsed_ldf_file(self, ldf_file: str) -> dict:
        """Get LDF file parsed using ldfparser"""
        return ldfparser.parseLDFtoDict(ldf_file)

    def _get_signals(self) -> list:
        """Get signals."""
        return [self.get_signal_by_name(signal['name']) for signal in self._parsed_data['signals']]
    
    def _get_frames(self) -> list:
        """Get frames."""
        return [self.get_frame_by_name(frame['name']) for frame in self._parsed_data['frames']]

    def get_frame_by_id(self, frame_id: str) -> dict:
        """Get frame by frame id."""
        for frame in self._parsed_data['frames']:
            if frame['frame_id'] == frame_id:
                return frame
        return None

    def get_frame_by_name(self, frame_name: str) -> dict:
        """Get frame by frame name."""
        for frame in self._parsed_data['frames']:
            if frame['name'] == frame_name:
                return frame
        return None

    def get_signal_by_name(self, name: str) -> dict:
        """Get signal by signal name."""
        for signal in self._parsed_data['signals']:
            if signal['name'] == name:
                values = self._get_signal_values_by_name(name)
                signal['values'] = values
                return signal
        return None

    def _get_signal_values_by_name(self, name: str) -> list:
        """Get signal values by signal name."""
        for encoding in self._parsed_data['signal_encoding_types']:
            if encoding['name'] == f"{name}_enc":
                return [value for value in encoding['values']]
        return None
