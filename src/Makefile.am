AM_CPPFLAGS = -I../include @ARCUS_CPPFLAGS@ -I@builddir@
AM_CXXFLAGS = -std=c++20 @FMT_CFLAGS@ @PROTOBUF_CFLAGS@

dist_noinst_DATA = ../Cura.proto
MOSTLYCLEANFILES = Cura.pb.cc Cura.ph.h
BUILT_SOURCES =

bin_PROGRAMS = CuraEngine
CuraEngine_SOURCES = \
	TopSurface.cpp \
	FffPolygonGenerator.cpp \
	infill.cpp \
	infill/ZigzagConnectorProcessor.cpp \
	infill/ImageBasedDensityProvider.cpp \
	infill/SierpinskiFill.cpp \
	infill/LightningLayer.cpp \
	infill/LightningDistanceField.cpp \
	infill/SubDivCube.cpp \
	infill/LightningTreeNode.cpp \
	infill/SierpinskiFillProvider.cpp \
	infill/GyroidInfill.cpp \
	infill/LightningGenerator.cpp \
	infill/NoZigZagConnectorProcessor.cpp \
	WallsComputation.cpp \
	SkirtBrim.cpp \
	TreeSupportTipGenerator.cpp \
	LayerPlan.cpp \
	communication/ArcusCommunication.cpp \
	communication/ArcusCommunicationPrivate.cpp \
	communication/Listener.cpp \
	communication/CommandLine.cpp \
	skin.cpp \
	raft.cpp \
	layerPart.cpp \
	SkeletalTrapezoidation.cpp \
	Application.cpp \
	Mold.cpp \
	ConicalOverhang.cpp \
	InsetOrderOptimizer.cpp \
	multiVolumes.cpp \
	PathOrderPath.cpp \
	MeshGroup.cpp \
	GCodePathConfig.cpp \
	LayerPlanBuffer.cpp \
	support.cpp \
	Preheat.cpp \
	main.cpp \
	TreeModelVolumes.cpp \
	gcodeExport.cpp \
	TreeSupport.cpp \
	Slice.cpp \
	progress/ProgressStageEstimator.cpp \
	progress/Progress.cpp \
	bridge.cpp \
	pathPlanning/LinePolygonsCrossings.cpp \
	pathPlanning/Comb.cpp \
	pathPlanning/TimeMaterialEstimates.cpp \
	pathPlanning/GCodePath.cpp \
	pathPlanning/NozzleTempInsert.cpp \
	InterlockingGenerator.cpp \
	sliceDataStorage.cpp \
	slicer.cpp \
	FffGcodeWriter.cpp \
	BeadingStrategy/BeadingStrategy.cpp \
	BeadingStrategy/DistributedBeadingStrategy.cpp \
	BeadingStrategy/LimitedBeadingStrategy.cpp \
	BeadingStrategy/WideningBeadingStrategy.cpp \
	BeadingStrategy/RedistributeBeadingStrategy.cpp \
	BeadingStrategy/OuterWallInsetBeadingStrategy.cpp \
	BeadingStrategy/BeadingStrategyFactory.cpp \
	PrimeTower.cpp \
	ExtruderTrain.cpp \
	SupportInfillPart.cpp \
	settings/Settings.cpp \
	settings/FlowTempGraph.cpp \
	settings/ZSeamConfig.cpp \
	settings/AdaptiveLayerHeights.cpp \
	settings/PathConfigStorage.cpp \
	timeEstimate.cpp \
	mesh.cpp \
	FffProcessor.cpp \
	SkeletalTrapezoidationGraph.cpp \
	utils/VoxelUtils.cpp \
	utils/ExtrusionJunction.cpp \
	utils/VoronoiUtils.cpp \
	utils/ExtrusionSegment.cpp \
	utils/ListPolyIt.cpp \
	utils/AABB.cpp \
	utils/SquareGrid.cpp \
	utils/polygon.cpp \
	utils/Date.cpp \
	utils/Simplify.cpp \
	utils/ToolpathVisualizer.cpp \
	utils/PolylineStitcher.cpp \
	utils/Point3.cpp \
	utils/gettime.cpp \
	utils/FMatrix4x3.cpp \
	utils/SVG.cpp \
	utils/ExtrusionLine.cpp \
	utils/PolygonsSegmentIndex.cpp \
	utils/polygonUtils.cpp \
	utils/socket.cpp \
	utils/AABB3D.cpp \
	utils/PolygonConnector.cpp \
	utils/LinearAlg2D.cpp \
	utils/ProximityPointLink.cpp \
	utils/PolygonsPointIndex.cpp \
	utils/MinimumSpanningTree.cpp \
	utils/ThreadPool.cpp \
	WallToolPaths.cpp \
	Scene.cpp
if ARCUS
CuraEngine_SOURCES += @builddir@/Cura.pb.cc
BUILT_SOURCES += Cura.pb.h
endif

CuraEngine_LDADD = @FMT_LIBS@ @PROTOBUF_LIBS@

%.pb.cc %.pb.h: ../%.proto
	$(PROTOC) --proto_path=@srcdir@/.. --cpp_out=@builddir@ $^
