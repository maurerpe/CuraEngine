AM_CPPFLAGS = -I../include @ARCUS_CPPFLAGS@ -I@builddir@
AM_CXXFLAGS = -std=c++20 @FMT_CFLAGS@ @PROTOBUF_CFLAGS@

dist_noinst_DATA = ../Cura.proto
MOSTLYCLEANFILES = Cura.pb.cc Cura.ph.h
BUILT_SOURCES =

bin_PROGRAMS = CuraEngine
CuraEngine_SOURCES = \
	main.cpp \
        Application.cpp \
        bridge.cpp \
        ConicalOverhang.cpp \
        ExtruderPlan.cpp \
        ExtruderTrain.cpp \
        FffGcodeWriter.cpp \
        FffPolygonGenerator.cpp \
        FffProcessor.cpp \
        gcodeExport.cpp \
        GCodePathConfig.cpp \
        infill.cpp \
        InterlockingGenerator.cpp \
        InsetOrderOptimizer.cpp \
        layerPart.cpp \
        LayerPlan.cpp \
        LayerPlanBuffer.cpp \
        mesh.cpp \
        MeshGroup.cpp \
        Mold.cpp \
        multiVolumes.cpp \
        path_ordering.cpp \
        PathAdapter.cpp \
        Preheat.cpp \
        PrimeTower/PrimeTower.cpp \
        PrimeTower/PrimeTowerNormal.cpp \
        PrimeTower/PrimeTowerInterleaved.cpp \
        raft.cpp \
        Scene.cpp \
        SkeletalTrapezoidation.cpp \
        SkeletalTrapezoidationGraph.cpp \
        skin.cpp \
        SkirtBrim.cpp \
        SupportInfillPart.cpp \
        Slice.cpp \
        sliceDataStorage.cpp \
        slicer.cpp \
        support.cpp \
        timeEstimate.cpp \
        SlicedUVCoordinates.cpp \
        TextureDataProvider.cpp \
        TopSurface.cpp \
        TreeSupportTipGenerator.cpp \
        TreeModelVolumes.cpp \
        TreeSupport.cpp \
        WallsComputation.cpp \
        WallToolPaths.cpp \
        BeadingStrategy/BeadingStrategy.cpp \
        BeadingStrategy/BeadingStrategyFactory.cpp \
        BeadingStrategy/DistributedBeadingStrategy.cpp \
        BeadingStrategy/LimitedBeadingStrategy.cpp \
        BeadingStrategy/RedistributeBeadingStrategy.cpp \
        BeadingStrategy/WideningBeadingStrategy.cpp \
        BeadingStrategy/OuterWallInsetBeadingStrategy.cpp \
        communication/ArcusCommunication.cpp \
        communication/ArcusCommunicationPrivate.cpp \
        communication/CommandLine.cpp \
        communication/EmscriptenCommunication.cpp \
        communication/Listener.cpp \
        infill/ImageBasedDensityProvider.cpp \
        infill/NoZigZagConnectorProcessor.cpp \
        infill/ZigzagConnectorProcessor.cpp \
        infill/LightningDistanceField.cpp \
        infill/LightningGenerator.cpp \
        infill/LightningLayer.cpp \
        infill/LightningTreeNode.cpp \
        infill/SierpinskiFill.cpp \
        infill/SierpinskiFillProvider.cpp \
        infill/SubDivCube.cpp \
        infill/GyroidInfill.cpp \
        pathPlanning/Comb.cpp \
        pathPlanning/GCodePath.cpp \
        pathPlanning/LinePolygonsCrossings.cpp \
        pathPlanning/NozzleTempInsert.cpp \
        pathPlanning/SpeedDerivatives.cpp \
        plugins/converters.cpp \
        progress/Progress.cpp \
        progress/ProgressStageEstimator.cpp \
        settings/AdaptiveLayerHeights.cpp \
        settings/FlowTempGraph.cpp \
        settings/MeshPathConfigs.cpp \
        settings/PathConfigStorage.cpp \
        settings/Settings.cpp \
        settings/ZSeamConfig.cpp \
        utils/AABB.cpp \
        utils/AABB3D.cpp \
        utils/channel.cpp \
        utils/Date.cpp \
        utils/ExtrusionJunction.cpp \
        utils/ExtrusionLine.cpp \
        utils/ExtrusionSegment.cpp \
        utils/gettime.cpp \
        utils/linearAlg2D.cpp \
        utils/ListPolyIt.cpp \
        utils/Matrix4x3D.cpp \
        utils/MinimumSpanningTree.cpp \
        utils/OBJ.cpp \
        utils/PolygonConnector.cpp \
        utils/PolygonsPointIndex.cpp \
        utils/PolygonsSegmentIndex.cpp \
        utils/polygonUtils.cpp \
        utils/PolylineStitcher.cpp \
        utils/Simplify.cpp \
        utils/SVG.cpp \
        utils/SquareGrid.cpp \
        utils/ThreadPool.cpp \
        utils/ToolpathVisualizer.cpp \
        utils/VoronoiUtils.cpp \
        utils/VoxelUtils.cpp \
        utils/MixedPolylineStitcher.cpp \
        utils/scoring/BestElementFinder.cpp \
        utils/scoring/CornerScoringCriterion.cpp \
        utils/scoring/DistanceScoringCriterion.cpp \
        utils/scoring/ExclusionAreaScoringCriterion.cpp \
        utils/scoring/PositionBasedScoringCriterion.cpp \
        utils/scoring/RandomScoringCriterion.cpp \
        utils/scoring/TextureScoringCriterion.cpp \
        geometry/Point2LL.cpp \
        geometry/Point3LL.cpp \
        geometry/Polygon.cpp \
        geometry/Shape.cpp \
        geometry/PointsSet.cpp \
        geometry/SingleShape.cpp \
        geometry/PartsView.cpp \
        geometry/LinesSet.cpp \
        geometry/Polyline.cpp \
        geometry/ClosedPolyline.cpp \
        geometry/MixedLinesSet.cpp

if ARCUS
CuraEngine_SOURCES += @builddir@/Cura.pb.cc
BUILT_SOURCES += Cura.pb.h
endif

CuraEngine_LDADD = @FMT_LIBS@ @PROTOBUF_LIBS@

%.pb.cc %.pb.h: ../%.proto
	$(PROTOC) --proto_path=@srcdir@/.. --cpp_out=@builddir@ $^
