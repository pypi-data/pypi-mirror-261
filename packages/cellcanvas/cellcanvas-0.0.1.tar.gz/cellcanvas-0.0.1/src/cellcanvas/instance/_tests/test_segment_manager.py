import pandas as pd
from napari.layers import Labels
import numpy as np
import pytest

from cellcanvas.instance.segment_manager import SegmentManager
from cellcanvas.constants import PAINTABLE_KEY, CLASS_KEY, UNASSIGNED_CLASS


def _make_labels_image() -> np.ndarray:
    label_image = np.zeros((10, 10, 10), dtype=int)
    label_image[0:5, 0:5, 0:5] = 1
    label_image[5:10, 5:10, 5:10] = 2
    return label_image


def test_feature_validation_no_features_table(make_napari_viewer):
    """Check that all necessary columns in the feature table are added
    when they are not initially present.
    """
    viewer = make_napari_viewer()
    labels_layer = viewer.add_labels(_make_labels_image())

    segment_manager = SegmentManager(labels_layer, viewer=viewer)
    features_table = labels_layer.features

    # check that the index column was added
    np.testing.assert_array_equal(np.array([0, 1, 2]), features_table["index"])

    # check that all label values (0, 1, 2) are set to paintable
    np.testing.assert_array_equal(
        np.array([True, True, True]),
        features_table[PAINTABLE_KEY]
    )

    # check that the class was assigned as "unassigned"
    np.testing.assert_array_equal(
        np.array([UNASSIGNED_CLASS, UNASSIGNED_CLASS, UNASSIGNED_CLASS]),
        features_table[CLASS_KEY]
    )


def test_feature_validation_invalid_features_table(make_napari_viewer):
    """Check that invalid features table raise an error."""
    viewer = make_napari_viewer()
    labels_layer = viewer.add_labels(_make_labels_image())

    labels_layer.features = pd.DataFrame({"not_index": [0, 1, 2]})

    with pytest.raises(ValueError):
        # if there is a features table, it should have an "index" column
        # with the instance IDs
        _ = SegmentManager(labels_layer, viewer=viewer)


def test_feature_validation_valid_features_table(make_napari_viewer):
    """Check that valid features table raise is not overwritten."""
    viewer = make_napari_viewer()
    labels_layer = viewer.add_labels(_make_labels_image())

    paintable_values = [False, False, False]
    class_values = ["background", "hello", "hello"]
    labels_layer.features = pd.DataFrame(
        {
            "index": [0, 1, 2],
            PAINTABLE_KEY: paintable_values,
            CLASS_KEY: class_values,
        }

    )

    segment_manager = SegmentManager(labels_layer, viewer=viewer)
    features_table = labels_layer.features

    # check that the paintable values were not overwritten
    np.testing.assert_array_equal(
        paintable_values,
        features_table[PAINTABLE_KEY]
    )

    # check that the class was assigned were not overwritten
    np.testing.assert_array_equal(
        class_values,
        features_table[CLASS_KEY]
    )


def test_paint_with_locked_features(make_napari_viewer):
    """Check that paint only paints paintable features."""
    viewer = make_napari_viewer()
    labels_layer = viewer.add_labels(_make_labels_image())
    initial_labels = labels_layer.data.copy()

    labels_layer.features = pd.DataFrame(
        {
            "index": [0, 1, 2],
            PAINTABLE_KEY: [True, False, True],
            CLASS_KEY: ["background", "locked", "paintable"],
        }
    )

    _ = SegmentManager(labels_layer, viewer=viewer)

    # lock paintable feature
    labels_layer.preserve_labels = True

    # Set the brush size to 1 to only paint over the selected pixel
    labels_layer.brush_size = 1

    # paint over a locked feature
    labels_layer.paint((1, 1, 1), 2)

    # check that the locked feature was not painted over
    np.testing.assert_array_equal(
        labels_layer.data, initial_labels
    )

    # paint over a paintable feature
    labels_layer.paint((6, 6, 6), 1)

    # check that the paintable feature was painted over
    assert labels_layer.data[6, 6, 6] == 1, "The paint operation should have painted over the paintable feature"


def test_fill_with_locked_features(make_napari_viewer):
    """Check that fill only paints paintable features."""
    viewer = make_napari_viewer()
    labels_layer = viewer.add_labels(_make_labels_image())
    initial_data = labels_layer.data.copy()

    labels_layer.features = pd.DataFrame(
        {
            "index": [0, 1, 2],
            PAINTABLE_KEY: [True, False, True],
            CLASS_KEY: ["background", "locked", "paintable"],
        }
    )

    _ = SegmentManager(labels_layer, viewer=viewer)

    # lock paintable feature
    labels_layer.preserve_labels = True

    # fill over a locked feature
    labels_layer.fill((1, 1, 1), 2)


    # check that the locked feature was not painted over
    np.testing.assert_array_equal(
        labels_layer.data, initial_data)
    
    # fill over a paintable feature
    labels_layer.fill((6, 6, 6), 1)

    # check that the paintable feature was painted over
    assert labels_layer.data[6, 6, 6] == 1, "The fill operation should have painted over the paintable feature"