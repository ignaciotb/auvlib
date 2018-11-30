#ifndef DRAPING_IMAGE_H
#define DRAPING_IMAGE_H

#include <bathy_maps/draping_generator.h>
#include <bathy_maps/patch_views.h>
#include <bathy_maps/sss_map_image.h>

struct draping_image : public draping_generator {
public:

    using BoundsT = Eigen::Matrix2d;

protected:

    BoundsT bounds;
    double resolution;
    const std::function<void(sss_map_image)>& save_callback;

public:

    draping_image(const Eigen::MatrixXd& V1, const Eigen::MatrixXi& F1, const Eigen::MatrixXd& C1,
        const Eigen::MatrixXd& V2, const Eigen::MatrixXi& F2, const Eigen::MatrixXd& C2,
        const xtf_sss_ping::PingsT& pings, const Eigen::Vector3d& offset,
        const csv_asvp_sound_speed::EntriesT& sound_speeds = csv_asvp_sound_speed::EntriesT(),
        const BoundsT& bounds, double resolution, const std::function<void(sss_map_image)>&);

    bool callback_pre_draw(igl::opengl::glfw::Viewer& viewer);
};

void drape_images(const Eigen::MatrixXd& V, const Eigen::MatrixXi& F,
                  const draping_image::BoundsT& bounds, const xtf_sss_ping::PingsT& pings,
                  const csv_asvp_sound_speed::EntriesT& sound_speeds,
                  double resolution, const std::function<void(sss_map_image)>& save_callback);

#endif // DRAPING_IMAGE_H