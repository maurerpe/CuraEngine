AM_CPPFLAGS = -I../include @ARCUS_CPPFLAGS@ -I@builddir@
AM_CXXFLAGS = -std=c++20 @FMT_CFLAGS@ @PROTOBUF_CFLAGS@

dist_noinst_DATA = ../Cura.proto
MOSTLYCLEANFILES = Cura.pb.cc Cura.ph.h
BUILT_SOURCES =

bin_PROGRAMS = CuraEngine
CuraEngine_SOURCES = \
	TreeSupportTipGenerator.cpp \
	PrimeTower/PrimeTower.cpp \
	PrimeTower/PrimeTowerInterleaved.cpp \
	PrimeTower/PrimeTowerNormal.cpp \
	Mold.cpp \
	timeEstimate.cpp \
	bridge.cpp \
	PrimeTower.cpp \
	LayerPlanBuffer.cpp \
	Slice.cpp \
	GCodePathConfig.cpp \
	TreeSupport.cpp \
	SkeletalTrapezoidation.cpp \
	raft.cpp \
	main.cpp \
	slicer.cpp \
	WallToolPaths.cpp \
	gcodeExport.cpp \
	skin.cpp \
	path_ordering.cpp \
	WallsComputation.cpp \
	ExtruderTrain.cpp \
	settings/MeshPathConfigs.cpp \
	settings/AdaptiveLayerHeights.cpp \
	settings/PathConfigStorage.cpp \
	settings/FlowTempGraph.cpp \
	settings/Settings.cpp \
	settings/ZSeamConfig.cpp \
	InterlockingGenerator.cpp \
	PathAdapter.cpp \
	Application.cpp \
	SkirtBrim.cpp \
	FffPolygonGenerator.cpp \
	sliceDataStorage.cpp \
	InsetOrderOptimizer.cpp \
	plugins/converters.cpp \
	infill.cpp \
	LayerPlan.cpp \
	BeadingStrategy/BeadingStrategy.cpp \
	BeadingStrategy/BeadingStrategyFactory.cpp \
	BeadingStrategy/LimitedBeadingStrategy.cpp \
	BeadingStrategy/OuterWallInsetBeadingStrategy.cpp \
	BeadingStrategy/DistributedBeadingStrategy.cpp \
	BeadingStrategy/WideningBeadingStrategy.cpp \
	BeadingStrategy/RedistributeBeadingStrategy.cpp \
	multiVolumes.cpp \
	progress/Progress.cpp \
	progress/ProgressStageEstimator.cpp \
	ExtruderPlan.cpp \
	geometry/Shape.cpp \
	geometry/Point3LL.cpp \
	geometry/ClosedPolyline.cpp \
	geometry/Point2LL.cpp \
	geometry/Polygon.cpp \
	geometry/MixedLinesSet.cpp \
	geometry/PartsView.cpp \
	geometry/LinesSet.cpp \
	geometry/PointsSet.cpp \
	geometry/Polyline.cpp \
	geometry/SingleShape.cpp \
	MeshGroup.cpp \
	utils/scoring/RandomScoringCriterion.cpp \
	utils/scoring/BestElementFinder.cpp \
	utils/scoring/ExclusionAreaScoringCriterion.cpp \
	utils/scoring/CornerScoringCriterion.cpp \
	utils/scoring/DistanceScoringCriterion.cpp \
	utils/PolygonsSegmentIndex.cpp \
	utils/polygonUtils.cpp \
	utils/Simplify.cpp \
	utils/linearAlg2D.cpp \
	utils/ToolpathVisualizer.cpp \
	utils/channel.cpp \
	utils/gettime.cpp \
	utils/PolylineStitcher.cpp \
	utils/VoronoiUtils.cpp \
	utils/PolygonsPointIndex.cpp \
	utils/ThreadPool.cpp \
	utils/ListPolyIt.cpp \
	utils/Matrix4x3D.cpp \
	utils/SVG.cpp \
	utils/AABB3D.cpp \
	utils/ExtrusionSegment.cpp \
	utils/Date.cpp \
	utils/MixedPolylineStitcher.cpp \
	utils/MinimumSpanningTree.cpp \
	utils/AABB.cpp \
	utils/ExtrusionLine.cpp \
	utils/PolygonConnector.cpp \
	utils/SquareGrid.cpp \
	utils/VoxelUtils.cpp \
	utils/ExtrusionJunction.cpp \
	FffProcessor.cpp \
	TopSurface.cpp \
	infill/LightningLayer.cpp \
	infill/LightningGenerator.cpp \
	infill/GyroidInfill.cpp \
	infill/LightningDistanceField.cpp \
	infill/SubDivCube.cpp \
	infill/SierpinskiFillProvider.cpp \
	infill/ImageBasedDensityProvider.cpp \
	infill/SierpinskiFill.cpp \
	infill/ZigzagConnectorProcessor.cpp \
	infill/NoZigZagConnectorProcessor.cpp \
	infill/LightningTreeNode.cpp \
	Scene.cpp

if ARCUS
CuraEngine_SOURCES += @builddir@/Cura.pb.cc
BUILT_SOURCES += Cura.pb.h
endif

CuraEngine_LDADD = @FMT_LIBS@ @PROTOBUF_LIBS@

%.pb.cc %.pb.h: ../%.proto
	$(PROTOC) --proto_path=@srcdir@/.. --cpp_out=@builddir@ $^
